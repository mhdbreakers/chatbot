import re

# Liste des mots interdits
prohibited_words = ['badword1', 'badword2', 'badword3']

# Fonction de filtrage
def filter_response(response):
    for word in prohibited_words:
        response = re.sub(r'\b' + word + r'\b', '[REDACTED]', response, flags=re.IGNORECASE)
    return response
