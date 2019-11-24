from typing import List

from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import patsy
import pandas as pd

model_selector = {
    "LinearRegression": LinearRegression(fit_intercept=False),
    "RandomForestRegressor": RandomForestRegressor(n_estimators=500),
}


def compare_models(df: pd.DataFrame, conf: dict) -> List[dict]:
    models_to_compare = conf["models_to_compare"]
    result = list()
    for model in models_to_compare:
        name, formula = list(model.keys())[0], list(model.values())[0]
        mod = model_selector[name]
        scores = cross_validate_from_formula(df, formula, mod)
        result.append({name: scores})
    return result


def cross_validate_from_formula(df: pd.DataFrame, formula: str, model):
    if formula == "all":
        formula = "price ~ " + "+".join(
            [col for col in df.drop("price", axis=1).columns]
        )
    y, x = patsy.dmatrices(formula, df, return_type="dataframe")
    scores = cross_validate(model, x, y.values.ravel(), cv=5, scoring="r2")
    return scores["test_score"]
