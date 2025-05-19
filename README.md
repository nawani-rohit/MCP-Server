# 🚀 SpaceX Launches MCP Server

A lightweight **Model Context Protocol (MCP)** server that fetches public SpaceX launch data and exposes three analytics endpoints.

| `analysisType` value | What it returns |
| -------------------- | --------------- |
| `countByYear`        | Launch counts for every year from the first SpaceX flight to the most recent. Missing years are zero-filled. |
| `successVsFailure`   | Total number of successful vs. failed launches. |
| `mostFrequentSite`   | Launch site used most often and its count. |

---

## 📂 Project Structure

spacex-mcp-server/
├── analysis.py
├── launch_data.py
├── main.py
├── requirements.txt
└── README.md

---

## ⚡ Quick Start

```bash
git clone https://github.com/<your-user>/spacex-mcp-server.git
cd spacex-mcp-server

python -m venv venv
source venv/bin/activate              # macOS / Linux
# .\venv\Scripts\Activate.ps1         # Windows

pip install -r requirements.txt
uvicorn main:app --reload --port 3000
````
---

## 🎯 API Endpoints

| Method | Path                     | Query Parameter                 | Description               |
| ------ | ------------------------ | ------------------------------- | ------------------------- |
| `GET`  | `/mcp/launches/analysis` | `analysisType=countByYear`      | Launch counts per year    |
|        |                          | `analysisType=successVsFailure` | Success vs failure totals |
|        |                          | `analysisType=mostFrequentSite` | Most-used launch site     |

---

## 🧪 Requests & Responses

> Replace `3000` if you run on a different port.

### 1️⃣ Launch Count by Year

```bash
curl "http://localhost:3000/mcp/launches/analysis?analysisType=countByYear"
```

```json
{
  "2006": 1,
  "2007": 1,
  "2008": 2,
  "2009": 1,
  "2010": 2,
  "2011": 0,
  "2012": 2,
  "2013": 3,
  "2014": 6,
  "2015": 7,
  "2016": 9,
  "2017": 18,
  "2018": 21,
  "2019": 13,
  "2020": 25
}
```

### 2️⃣ Successful vs Failed Launches

```bash
curl "http://localhost:3000/mcp/launches/analysis?analysisType=successVsFailure"
```

```json
{
  "successful_launches": 191,
  "failed_launches": 9
}
```

### 3️⃣ Most Frequent Launch Site

```bash
curl "http://localhost:3000/mcp/launches/analysis?analysisType=mostFrequentSite"
```

```json
{
  "site": "CCAFS SLC 40",
  "launch_count": 52
}
```
