import sqlite3
import re

def extract_budget_and_validity(message):
    budget = None
    days = None
    found_budget = re.search(r'(?:₹\s?)(\d{2,5})', message)
    if not found_budget:
        found_budget = re.search(r'\b(\d{2,5})\b', message)
    if found_budget:
        budget = int(found_budget.group(1))
    days_match = re.search(r'(\d{1,3})\s*(?:days|Days)', message)
    if days_match:
        days = int(days_match.group(1))
    return budget, days

def process_message(message):
    message = message.lower().replace(",", " ").replace("and", " ")
    budget, validity_days = extract_budget_and_validity(message)
    
    sim_name = None
    if "airtel" in message:
        sim_name = "Airtel"
    elif "jio" in message:
        sim_name = "Jio"
    elif "vi" in message or "vodafone" in message:
        sim_name = "VI"
    
    response = ""
    if sim_name and budget is not None and validity_days is not None:
        conn = sqlite3.connect("plans.db")
        cur = conn.cursor()
        cur.execute(
            """
            SELECT name, data_limit, validity, price, benefits 
            FROM plans
            WHERE name=?
              AND price<=?
              AND CAST(SUBSTR(validity, 1, INSTR(validity, ' ') - 1) AS INTEGER) >= ?
            """,
            (sim_name, budget, validity_days)
        )
        rows = cur.fetchall()
        conn.close()
        if rows:
            for row in rows:
                response += f"Data: {row[1]}, Validity: {row[2]}, Price: ₹{row[3]}, Benefits: {row[4]}\n"
        else:
            response = " No plans found matching your requirements."
    else:
        response = " Please specify SIM name, budget, and validity days."
    return response.strip()
