# Data Card

## Dataset

Expected file:

```text
data/raw/CA2-Energy-Consumption-Data.csv
```

The raw dataset is not included in this repository. This avoids committing
coursework-provided data unless redistribution rights are confirmed.

## Schema

| Column | Required | Type | Validation |
| --- | --- | --- | --- |
| `DATE` | Yes | Date | Parsed day-first; exactly one consecutive observation per month. |
| `Gas Consumption (tons)` | Yes | Numeric | Must be strictly positive. |
| `Electricity Consumption (MWh)` | Yes | Numeric | Must be strictly positive. |
| `Water Consumption (tons)` | Yes | Numeric | Must be strictly positive. |

## Preparation

The reusable loader:

1. Reads the CSV.
2. Validates required columns.
3. Parses `DATE`.
4. Converts target columns to numeric values.
5. Drops rows with missing required values.
6. Sorts by date and sets `DATE` as the index.
7. Rejects missing months or multiple observations in the same month.
8. Checks that target values are positive for log transformation.

## Known Constraints

- Forecast quality depends on the representativeness of the historical period.
- External drivers such as pricing, policy, holidays, weather, and population
  changes are not included in the current dataset contract.
- Removing outliers may change temporal spacing; use that option deliberately.

## Privacy and Licensing

Do not commit the raw CSV unless redistribution is explicitly allowed. If a
public dataset replaces the coursework data, document its source, licence, and
collection methodology here.
