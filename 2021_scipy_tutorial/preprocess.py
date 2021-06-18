import pandas as pd
from pathlib import Path
import os

data_path = Path(f"{os.getcwd()}/data")

def main():
    df = (pd.read_csv(data_path / "diabetic_data.csv")
        .rename(columns={"diag_1": "primary_diagnosis"}))
    # Create Outcome variables
    df.loc[:, "readmit_30_days"] = (df["readmitted"] == "<30")
    df.loc[:, "readmit_binary"] = (df["readmitted"] != "NO")
    # Replace missing values and re-code categories
    df.loc[:,"age"] = df.age.replace({"?": ""})
    df.loc[:,"payer_code"] = df["payer_code"].replace({"?", "Unknown"})
    df.loc[:,"medical_specialty"] = df["medical_specialty"].replace({"?": "Missing"})
    df.loc[:, "race"] = df["race"].replace({"?": "Unknown"})

    df.loc[:, "admission_source_id"] = df["admission_source_id"].replace({1: "Referral", 2: "Referral", 3: "Referral", 7: "Emergency"})
    df.loc[:, "age"] = df["age"].replace( ["[0-10)", "[10-20)", "[20-30)"], "30 years or younger")
    df.loc[:, "age"] = df["age"].replace(["[30-40)", "[40-50)", "[50-60)"], "30-60 years")
    df.loc[:, "age"] = df["age"].replace(["[60-70)", "[70-80)", "[80-90)"], "Over 60 years")
    
    # Clean various medical codes
    df.loc[:, "discharge_disposition_id"] = (df.discharge_disposition_id
                                            .apply(lambda x: "Discharged to Home" if x==1 else "Other"))

    df.loc[:, "admission_source_id"] = df["admission_source_id"].apply(lambda x: x if x in ["Emergency", "Referral"] else "Other")
    # Re-code Medical Specialties and Primary Diagnosis
    specialties = [
        "Missing",
        "InternalMedicine",
        "Emergency/Trauma",
        "Family/GeneralPractice",
        "Cardiology",
        "Surgery"
    ]
    df.loc[:, "medical_specialty"] = df["medical_specialty"].apply(lambda x: x if x in specialties else "Other")
    #
    df.loc[:, "primary_diagnosis"] = df["primary_diagnosis"].replace(
        regex={
            "[7][1-3][0-9]": "Musculoskeltal Issues",
            "250.*": "Diabetes",
            "[4][6-9][0-9]|[5][0-1][0-9]|786": "Respitory Issues",
            "[5][8-9][0-9]|[6][0-2][0-9]|788": "Genitourinary Issues"
        }
    )
    diagnoses = ["Respitory Issues", "Diabetes", "Genitourinary Issues", "Musculoskeltal Issues"]
    df.loc[:, "primary_diagnosis"] = df["primary_diagnosis"].apply(lambda x: x if x in diagnoses else "Other")



    #Binarize and bin features
    df.loc[:, "medicare"] = (df.payer_code == "MC")
    df.loc[:, "medicaid"] = (df.payer_code == "MD")

    df.loc[:, "had_emergency"] = (df["number_emergency"] > 0)
    df.loc[:, "had_inpatient_days"] = (df["number_inpatient"] > 0)
    df.loc[:, "had_outpatient_days"] = (df["number_outpatient"] > 0)

    # Save DataFrame
    cols_to_keep = ["race","gender","age","discharge_disposition_id","admission_source_id","time_in_hospital",
        "medical_specialty","num_lab_procedures","num_procedures","num_medications","primary_diagnosis","number_diagnoses","max_glu_serum","A1Cresult","insulin","change",
        "diabetesMed", "medicare", "medicaid", "had_emergency", "had_inpatient_days", "had_outpatient_days", "readmitted","readmit_binary","readmit_30_days"]

    final_df = df.loc[:, cols_to_keep]
    final_df.to_csv(data_path / "diabetic_preprocessed.csv", index=False)

if __name__ == "__main__":
    main()