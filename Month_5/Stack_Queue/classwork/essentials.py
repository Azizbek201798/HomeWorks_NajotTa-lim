class stack:
    def __init__(self):
        self.__stack = []

    def push(self,item,x):
        self.__stack.insert(x,item)

    def pop(self,z : int):
        if len(item) % 2 == 0:
            self.__stack.pop(z)

    def get_info(self):
        print(self.__stack)

if __name__ == "__main__":
    st = stack()
    for x in range(5):
        item = input("Satr kiriting : ")
        st.push(item,x)
        st.pop(x)
    
    st.get_info()

    # ax2 + bx + c = 0