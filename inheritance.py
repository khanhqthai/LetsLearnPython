class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age  = data_str.split(",")
        return cls(first, last, int(age))
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1
    
    def logout(self):
        User.active_users += -1
        return f"{self.first} has logged out"
    
    def full_name(self):
        return f"{self.first} {self.last}"
        

class Moderator(User):
        
    def __init__(self, first, last, age, community):
        super().__init__(first,last, age)
        self.community = community
    
    def remove_post(self):
        return f"{self.full_name()} remove post from the {self.community} community"
        
tim = Moderator("tim","horn", 36, "nba")

print(tim.full_name())
print(tim.community )