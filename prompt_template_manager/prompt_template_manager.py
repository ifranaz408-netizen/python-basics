import json 
class prompt:
    def __init__(self,id,title,category,prompt_text,tags,favorite):
        self.id=id
        self.title=title
        self.category=category
        self.prompt_text=prompt_text
        self.tags=tags
        self.favorite=favorite
    def display(self):
        print("ID:",self.id)
        print("TITLE:",self.title)
        print("CATEGORY:",self.category)
        print("PROMPT_TEXT:",self.prompt_text)
        print("TAGS:",self.tags)
        print("FAVORITE:", self.favorite)
    def to_dict(self):
        return{
            "id":self.id,"title":self.title,"category":self.category,"prompt_text":self.prompt_text,"tags":self.tags,"favorite":self.favorite
        }
class promptmanager:
    def __init__(self):
        self.prompts=[]
        self.load_prompts()
    def load_prompts(self):
      try:
        with open ("prompts.json","r") as file:
          data= json.load(file)
        for record in data :
           new_prompt = prompt(
                    record["id"],
                    record["title"],
                    record["category"],
                    record["prompt_text"],
                    record["tags"],
                    record["favorite"]
                )

           self.prompts.append(new_prompt)
      except FileNotFoundError:
        self.prompts = []

      except json.JSONDecodeError:
         self.prompts = []

    def  save_prompts(self):

        with open("prompts.json", "w") as file:
            data = []

            for prompt in self.prompts:
                data.append(prompt.to_dict())

            json.dump(data, file, indent=4)
    def add_prompt(self):
        new_id=input("enter your id:")
        new_title=input("enter your title:")
        new_category=input("enter your category:")
        new_prompt_text=input("enter your prompt_text:")
        new_tags=input("enter your tags:")
        new_favorite = False
        newprompt=prompt(new_id,new_title,new_category,new_prompt_text,new_tags,new_favorite)
        self.prompts.append(newprompt)
        self.save_prompts()
        print("Prompt Added Successfully!")
    def view_prompt(self):
        if not self.prompts:
            print("No Prompt Records Found!")
        else:
            for prompt in self.prompts:
                prompt.display()
                print("-" * 35)
                print()
    def search_prompt(self):
        user_id=input("enter your id:")
        found =False
        for prompt in self.prompts:
            if prompt.id==user_id:
                print("prompt found!!")
                prompt.display()
                found=True
                break
        if found==False:
            print("prompt not found!!")
    def update_prompt(self):
        user_id=input("enter your id:")
        found =False
        for prompt in self.prompts:
            if prompt.id==user_id:
                print("prompt found!!")
                prompt.display()
                prompt.title=input("enter new title:")
                prompt.category=input("enter new category:")
                prompt.prompt_text=input("enter new prompt_text:")
                prompt.tags=input("enter new tags:")
                self.save_prompts()
                print("prompt updated!!")
                found=True
                break
        if found==False:
            print("prompt not found!!")
    def delete_prompt(self):
        user_id=input("enter your id:")
        found =False
        for prompt in self.prompts:
            if prompt.id==user_id:
                print("prompt found!!")
                prompt.display()
                self.prompts.remove(prompt)
                self.save_prompts()
                found=True
                break
        if found==False:
            print("prompt not found!!")
    def view_by_category(self):
        user_category=input("enter category:")
        found =False
        for prompt in self.prompts:
                    if prompt.category==user_category:
                        print("Category found!!")
                        prompt.display()
                        found=True
                        
        if found==False:
                    print("Category not found!!")
    def search_by_tag(self):
        user_tags=input("enter tags:")
        found =False
        for prompt in self.prompts:
            if user_tags.strip().lower() in prompt.tags.split(","):
                print("Tags found!!")
                prompt.display()
                print("-" * 35)
                print()
                found=True
        if found==False:
                     print("Tags not found!!")
    def Favorite_Prompt(self):
        user_id=input("enter tour id:")
        found =False
        for prompt in self.prompts:

            if prompt.id==user_id:
                print("id found!!")
                prompt.display()
                print("_" * 35)
                print()
                found=True
                prompt.favorite = True
                print("favorite added sucessfully!!")
                self.save_prompts()
        if found==False:
            print("id not found!!")
    def View_Favorites(self):
        found = False

        for prompt in self.prompts:

            if prompt.favorite== True:
             prompt.display()
             print("_" * 35)
             print()
             found = True

        if found == False:
            print("No Favorite Records Found!")
    def Duplicate_Prompt(self):
        print("Which prompt do you want to copy??")
        user_id = input("Enter ID: ")
        found = False

        for p in self.prompts:
            if p.id == user_id:
                print("Prompt found!!")
                p.display()

                new_id = input("Enter new ID: ")

                new_prompt = prompt(
                    new_id,
                    p.title,
                    p.category,
                    p.prompt_text,
                    p.tags,
                    p.favorite
                )

                self.prompts.append(new_prompt)
                self.save_prompts()

                print("Prompt duplicated successfully!!")
                found = True
                break

        if found == False:
            print("ID not found!!")

manager=promptmanager()
while True:
    print("="*45)
    print(  "welcome to my project :PROMPT TEMPLATE MANAGER"   )
    print("="*45)
    print("1. Add prompt")
    print("2. View prompt")
    print("3. Search prompt")
    print("4. Update prompt")
    print("5. Delete prompt")
    print("6. View by Category")
    print("7. Search by Tags")
    print("8. Favorite Prompt")
    print("9. View Favorites")
    print("10. Duplicate Prompt")
    print("11. Exit")
    choice=input("enter your choice(1 to 11): ")
    if choice == "1":
        manager.add_prompt()
    elif choice == "2":
        manager.view_prompt()
        input("\nPress Enter to continue...")
    elif choice == "3":
        manager.search_prompt()
        input("\nPress Enter to continue...")
    elif choice == "4":
        manager.update_prompt()
        input("\nPress Enter to continue...")
    elif choice == "5":
        manager.delete_prompt()
        input("\nPress Enter to continue...")
    elif choice == "6":
            manager.view_by_category()
            input("\nPress Enter to continue...")
    elif choice == "7":
            manager.search_by_tag()
            input("\nPress Enter to continue...")
    elif choice == "8":
            manager.Favorite_Prompt()
            input("\nPress Enter to continue...")
    elif choice == "9":
            manager.View_Favorites()
            input("\nPress Enter to continue...")
    elif choice == "10":
            manager.Duplicate_Prompt()
            input("\nPress Enter to continue...")
    elif choice == "11":
        print("Exiting program. Goodbye!")
        input("\nPress Enter to continue...")
        break
    else:
       print("Invalid choice! Please try again.")




        
