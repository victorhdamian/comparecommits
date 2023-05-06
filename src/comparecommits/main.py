import git_interface

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

menu_options = {
    1: 'list commits',
    2: 'compare commits',
    3: 'exit',
}

def list_commits(org, repo):
    for commit in git_interface.get_commits(org, repo):
        print("Commit SHA: ", commit["sha"])
        print("Commit Comment: ", commit["commit"]["message"])
        print("==========")

def compare_commits(org, repo, base, head):
    result = git_interface.compare_commits(org, repo, base, head)
    print("base(master/main/default branch) commit sha: ", result["base_commit"]["sha"])
    print("base commit comment: ", result["base_commit"]["commit"]["message"])
    print("==========")
    print("merge base (head of branch to be merge) commit sha: ", result["merge_base_commit"]["sha"])
    print("merge base commit comment: ", result["merge_base_commit"]["commit"]["message"])

def option3():
    print('Handle option \'Option 3\'')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    org = input("please enter github organozation ie.: aws-ia : ")
    repo = input("please enter github repository name ie.: terraform-aws-eks-blueprints : ")
    head = input("please enter merge base sha ie.: e7040b657d95be543ed9c46187126ee8afe3a927 : ")
    base = input("please enter base sha dbd9ca385b0f8055e9aab1a54f76e0e74159fbe4 : ")

    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
            if option == 1:
               list_commits(org, repo)
            elif option == 2:
                compare_commits(org, repo, base, head)
            elif option == 3:
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print('Wrong input. Please enter a number ...')
            raise




