class Author:
    def __init__(self, 
                 name: str,
                 id = 0) -> None:
        self.id = id
        self.first_name: str = ""
        self.last_name: str = ""
        self.get_name_parts(name)
    
        
    def get_name_parts(self, name: str):
        name_parts = name.split(" ")

        if len(name_parts)>2:
            self.first_name, *self.last_name = name_parts
        else: 
            self.first_name, self.last_name = name_parts

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

