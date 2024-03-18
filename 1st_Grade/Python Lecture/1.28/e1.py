user_info = { 'id':'software', 'pw':'python' }

Id = input()
Pw = input()

if Id != user_info['id']:
    print("ID Mismatch!")
elif Pw !=  user_info['pw']:
    print("PW Mismatch!")
else:
    print("Success in Login")

