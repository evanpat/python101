from replit import db

#print(type(db.keys()))


if "a" not in db.keys():
  db["a"] = 1;
else:
  db["a"] += 1;

print(db["a"])
