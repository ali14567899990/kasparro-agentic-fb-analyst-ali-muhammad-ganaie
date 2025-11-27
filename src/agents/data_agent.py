import pandas as pd

class DataAgent:
    def __init__(self, data_csv, config):
        self.data_csv = data_csv
        self.config = config
        self.df = None

    def load_data(self):
        # Load CSV
        self.df = pd.read_csv(self.data_csv)

        # Convert date if needed
        if "date" in self.df.columns:
            self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")

        # Derived metrics
        self.df["CTR"] = self.df["clicks"] / self.df["impressions"]
        self.df["ROAS"] = self.df["revenue"] / self.df["spend"]

        return self.df

    def summarize(self):
        if self.df is None:
            self.load_data()

        return {
            "total_campaigns": self.df["campaign_name"].nunique(),
            "total_spend": self.df["spend"].sum(),
            "total_revenue": self.df["revenue"].sum(),
            "avg_ROAS": self.df["ROAS"].mean(),
            "avg_CTR": self.df["CTR"].mean()
        }
