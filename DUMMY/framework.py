frameworks=[
    {"fwname":"django","language":"python","rating":5},#fw
    {"fwname": "flask", "language": "python", "rating": 3},
    {"fwname": "angular", "language": "typescript", "rating": 5},
    {"fwname": "react", "language": "javascript", "rating": 4},
    {"fwname": "spring", "language": "java", "rating": 4},
    {"fwname": "ASP", "language": "c#", "rating": 5},

]

language=[fw.get("fwname")for fw in frameworks if fw.get("rating")>4]
print(language)

py_fws=[fw.get("fwname") for fw in frameworks if fw.get("language")=="python"]
print(py_fws)

most_rated=max(frameworks,key=lambda fw:fw.get("rating"))
print(most_rated)

min_rated=min(frameworks,key=lambda fw:fw.get("rating"))
print(min_rated)
