class employee:
    name=""
    emp_no=0

    def data(self):
        print("name is", self.name)
        print("employee number is:",self.emp_no)
sm = employee()
sm.name='ashutosh'
sm.emp_no=1234234
sm.data()
