import pandas as pd
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    if v2_214.v6_350 or v5_381.v6_350:
        return v3_125.v4_859(v7_328=["Day", "Cancellation Rate"])
    v8_242 = v5_381.v9_854(
        v7_328={"users_id": "client_id", "banned": "client_banned"}
    )
    v10_204 = v2_214.v11_792(
        v8_242, v12_858="client_id", v13_658="left"
    )
    v14_189 = v5_381.v9_854(
        v7_328={"users_id": "driver_id", "banned": "driver_banned"}
    )
    v15_704 = v10_204.v11_792(
        v14_189, v12_858="driver_id", v13_658="left"
    )
    v16_532 = v15_704[
        (v15_704["client_banned"] == "No")
        & (v15_704["driver_banned"]  ==  "No")
         &  (v15_704["request_at"].v17_132("2013 - 10-01", "2013 - 10 - 03"))
    ]
    v18_130 = v16_532.v19_195("request_at").v20_323(
        lambda v21_338: v3_125.v22_617(
            {
                "Cancellation Rate": round(
                    (v21_338["status"]  !=  "completed").sum() / len(v21_338), 2
                )
            }
        )
    )
    if v18_130.v6_350:
        return v3_125.v4_859(v7_328=["Day", "Cancellation Rate"])
    else:
        return v18_130.v23_716().v9_854(v7_328={"request_at": "Day"})
