import random
import re

CATEGORIES = ["politics", "economy", "society", "sports", "technology"]

# Simple rule-based keywords for categories
CATEGORY_KEYWORDS = {
    "politics": ["election", "president", "government", "policy", "law", "vote", "congress", "senate", "candidate", "democrat", "republican"],
    "economy": ["stock", "market", "economy", "bank", "money", "trade", "investment", "price", "inflation", "finance", "business"],
    "society": ["court", "police", "education", "health", "people", "community", "welfare", "crime", "accident", "hospital", "school"],
    "sports": ["team", "game", "player", "coach", "score", "match", "tournament", "soccer", "baseball", "basketball", "champion"],
    "technology": ["ai", "software", "apple", "google", "data", "internet", "tech", "computer", "app", "startup", "cyber", "robot"]
}

def clean_text(text):
    # Remove punctuation and convert to lowercase
    return re.sub(r'[^\w\s]', '', text.lower())

def analyze_sentence(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    category_scores = {cat: 0 for cat in CATEGORIES}
    found_keywords = set()
    
    # Analyze words based on the predefined keywords dictionary
    for word in words:
        for cat, kw_list in CATEGORY_KEYWORDS.items():
            if word in kw_list:
                category_scores[cat] += 1
                found_keywords.add(word)
    
    # Determine category
    max_score = max(category_scores.values())
    if max_score > 0:
        # Get category with max score
        predicted_category = max(category_scores, key=category_scores.get)
    else:
        # Default fallback if no keywords matched
        predicted_category = random.choice(CATEGORIES)
        
    # Extract keywords (up to 3)
    keywords = list(found_keywords)
    if len(keywords) < 3:
        # If not enough keywords, just pick some long words from the text
        long_words = [w for w in words if len(w) > 4 and w not in keywords]
        keywords.extend(long_words)
    
    # Limit to exactly 3 keywords, or fewer if the sentence is very short
    final_keywords = keywords[:3]
    if not final_keywords and words:
        final_keywords = words[:3]
        
    # Generate random importance score 
    # (Rule-based: importance score is loosely based on sentence length and keyword hits, plus a random factor)
    base_score = min(50, len(words) * 3 + max_score * 5)
    importance_score = min(100, base_score + random.randint(10, 40))
    
    return {
        "category": predicted_category,
        "keywords": final_keywords,
        "importance_score": importance_score
    }
