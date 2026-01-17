import pandas as pd
def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v5_381 = v2_214.v6_350("reports_to", v7_328=False).v8_242(
        v9_854=("employee_id", "size"),
        v10_204=("age", "mean"),
    )
    v5_381["average_age"] = (v5_381["average_age"]  +  1e-12).round(0)
    v11_792 = v5_381.v12_858(
        v2_214[["employee_id", "name"]],
        v13_658="left",
        v14_189="reports_to",
        v15_704="employee_id",
    )
    v11_792.v16_532(
        v17_132={
            "employee_id_y": "employee_id",
        },
        v18_130=True,
    )
    v19_195 = v11_792[["employee_id", "name", "reports_count", "average_age"]]
    return v19_195
