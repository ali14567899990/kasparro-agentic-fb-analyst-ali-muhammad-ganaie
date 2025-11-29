import pandas as pd
from src.utils import (
    get_logger,
    validate_schema,
    detect_schema_drift
)

class DataAgent:
    def __init__(self, data_csv, config):
        self.data_csv = data_csv
        self.config = config
        self.df = None
        self.logger = get_logger("DataAgent")

        # Expected schema fields
        self.expected_fields = [
            "date",
            "campaign_name",
            "impressions",
            "clicks",
            "spend",
            "revenue"
        ]

    def load_data(self):
        self.logger.info(f"Loading data from: {self.data_csv}")

        # Load CSV file
        self.df = pd.read_csv(self.data_csv)

        # ---------------------------
        # VALIDATE SCHEMA
        # ---------------------------
        valid, missing = validate_schema(self.df, self.expected_fields)

        if not valid:
            self.logger.error(f"Schema validation failed. Missing fields: {missing}")
            raise ValueError(f"Input CSV is missing required fields: {missing}")

        # ---------------------------
        # DETECT SCHEMA DRIFT
        # ---------------------------
        drift_report = detect_schema_drift(self.df, self.expected_fields)
        self.logger.info(f"Schema drift report: {drift_report}")

        # ---------------------------
        # PROCESS DATA
        # ---------------------------
        # Convert date
        if "date" in self.df.columns:
            self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")

        # Derived metrics
        try:
            self.df["CTR"] = self.df["clicks"] / self.df["impressions"]
            self.df["ROAS"] = self.df["revenue"] / self.df["spend"]
        except Exception as e:
            self.logger.error(f"Error calculating derived metrics: {e}")
            raise

        self.logger.info(f"Loaded dataset with {len(self.df)} rows.")
        return self.df

    def summarize(self):
        # Auto-load data if needed
        if self.df is None:
            self.load_data()

        self.logger.info("Summarizing dataset...")

        summary = {
            "total_campaigns": self.df["campaign_name"].nunique(),
            "total_spend": self.df["spend"].sum(),
            "total_revenue": self.df["revenue"].sum(),
            "avg_ROAS": self.df["ROAS"].mean(),
            "avg_CTR": self.df["CTR"].mean()
        }

        self.logger.info(f"Summary: {summary}")
        return summary
