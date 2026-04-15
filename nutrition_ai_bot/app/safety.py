# app/safety.py

def apply_safety_filters(query: str):
    medical_keywords = ["dose", "medicine", "prescription"]
    if any(word in query.lower() for word in medical_keywords):
        return False
    return True
