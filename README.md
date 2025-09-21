# Data Engineer Assignment

This repository demonstrates a data engineering workflow using Python, PostgreSQL, SQLAlchemy, pandas, and Plotly. It covers data extraction, loading, transformation, and visualization for message and status data.

---

## 📁 Project Structure

```
data-engineer-assignment/
│
├── data/                   # Raw CSV files (messages.csv, statuses.csv)
|── images/                 # Visualization images after plotting in python using plotly
├── scripts/
│   ├── db.py               # Loads DB credentials and creates SQLAlchemy engine
│   ├── extraction.py       # Creates tables in PostgreSQL
│   ├── loading.py          # Loads CSV data into tables
│   ├── transform.py        # Creates and populates the message_enriched table
│   └── plots.py            # Generates visualizations from enriched data
├── sql/
│   └── message_enriched.sql # SQL for creating the message_enriched table
|   └── data_qulaity_checker.sql # SQL for duplicated records and data qulaity checks.
├── .env                    # Environment variables (not committed)
├── requirement.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Quickstart

### 1. Clone the repository

```sh
git clone https://github.com/abhi19992/Data-Pipeline-Healthcare-Project.git
cd data-engineer-assignment
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Set up PostgreSQL

- Ensure PostgreSQL is running locally.
- Create a database (e.g., `noora_health_db`).

### 4. Configure environment variables

Create a `.env` file in the scripts:

```
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=noora_health_db
```

**Note:**  
`.env` is ignored by git for security.

### 5. Prepare data

Place `messages.csv` and `statuses.csv` in the `data/` folder.

---

## 🛠️ Workflow

1. **Create tables in PostgreSQL**
    ```sh
    python scripts/extraction.py
    ```

2. **Load CSV data into tables**
    ```sh
    python scripts/loading.py
    ```

3. **Transform data (create `message_enriched` table)**
    ```sh
    python scripts/transform.py
    ```

4. **Generate plots and visualizations**
    ```sh
    python scripts/plots.py
    ```

---

## 📜 Script Descriptions

- **db.py**  
  Loads database credentials from `.env` and creates a SQLAlchemy engine.

- **extraction.py**  
  Creates the `messages` and `statuses` tables in PostgreSQL.

- **loading.py**  
  Loads CSV data from the `data/` folder into the respective tables.

- **transform.py**  
  Executes the SQL in `sql/message_enriched.sql` to create the `message_enriched` table.

- **plots.py**  
  Generates interactive visualizations using Plotly from the enriched data.
  The output files are stored in images folder as well.

---

## Visualization Results
- **1.**
   Active & Total Users Per Week
   ---------------------------------
  
<img width="2864" height="1860" alt="image" src="https://github.com/user-attachments/assets/963dad36-1283-4a3b-82ba-c5bbd4a2ecd6" />

- **2.**
   Fraction of non-failed outbound messages read
   ---------------------------------

<img width="2876" height="1788" alt="image" src="https://github.com/user-attachments/assets/4b40a917-0389-4aed-a8ae-cfc4cceb8dd1" />

- **3.**
    Time to read distribution
   ---------------------------------
<img width="2790" height="1830" alt="image" src="https://github.com/user-attachments/assets/31489b8a-2bfd-4ac0-9fd3-894f43d95652" />

- **4.**
    Outbound messages in last week by status
   ---------------------------------
<img width="2844" height="1850" alt="image" src="https://github.com/user-attachments/assets/61c2255c-07fb-4231-8971-093d53b477f8" />

## 📝 Notes

- All credentials are managed via the `.env` file for security.
- The SQL logic for enrichment is in `sql/message_enriched.sql`.
- Visualizations are interactive and will open in your browser.

---

**Author:**  
Abhijeet
