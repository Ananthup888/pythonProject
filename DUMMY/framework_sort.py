frameworks=[
    {"fwname":"django","language":"python","rating":5},#fw
    {"fwname": "flask", "language": "python", "rating": 3},
    {"fwname": "angular", "language": "typescript", "rating": 5},
    {"fwname": "react", "language": "javascript", "rating": 4},
    {"fwname": "spring", "language": "java", "rating": 4},
    {"fwname": "ASP", "language": "c#", "rating": 5},

]

frameworks.sort(key=lambda fw:fw.get("rating"))
print(frameworks)

frameworks.sort(key=lambda fw:fw.get("rating"),reverse=True)
print(frameworks)
