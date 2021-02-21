def authenticate_user(uname, pwd):
	user_db = {
	"user_1": "pwd_11",
	"user_2": "pwd_21",
	"user_3": "pwd_31",
	"user_4": "pwd\n1234",
	"user_5": "$pwd#12$"
	}

	def validate_user(uname):
		f=0
		for i in user_db:
			if i==uname:
				f=1
		return f


	def check_password(uname,pwd):
		if(pwd==user_db[uname]):
			return True
		else:
			return False

	if(validate_user(uname)==1):
		if check_password(uname,pwd) :
			print("User Authenticated")
		else:
			print("Incorrect Password")

	else:
		print("Username Does Not Exist")

if __name__ == '__main__':
	authenticate_user("user1","pwd_11")
	authenticate_user("user_1","pwd_123")
	authenticate_user("user_4","pwd\n1234")
	