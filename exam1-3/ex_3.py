import hashlib

class Member():
    def __init__(self, name, username, password) -> None:
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"{self.name}: {self.username}")

class Post():
    def __init__(self, title, content, author) -> None:
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print('-'*30)
        print(f"title: {self.title}\n\n{self.content} \n\t-{self.author}-")

class Community():
    
    def __init__(self) -> None:
        self.members = []
        self.posts = []
        self.member_format = {
            '회원 이름': None,
            '회원 아이디': None,
            '회원 비밀번호': None,
        }
        self.post_format = {
            '제목': None,
            '내용': None,
            '회원 이름': None,
        }
        self.commands = ['회원 목록', '회원 가입', '게시글 목록', '게시글 추가', '게시글 검색', '나가기']
        self.command_dict = {
            '1': self.user_list,
            '2': self.user_append,
            '3': self.post_list,
            '4': self.post_append,
            '5': self.post_search,
            '6': self.quit,
        }

    def print_opt(self):
        print('\n<< 옵션 목록 >>\n(숫자로 입력하세요)')
        for i, opt in enumerate(self.commands):
            print(f'{i+1}. '+opt)

    def execute(self, ins):
        print('='*30)
        if 1 <= int(ins) <= len(self.commands): 
            command = self.command_dict[ins]
            return command()
        else: 
            print("다시 입력하세요.")
            return True
    
    def user_list(self):
        for member in self.members:
            member.display()

        return True

    def hashing(self, password):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()

    def user_append(self):
        while True:
            for format in self.member_format.keys():
                self.member_format[format] = input(f'{format}을 입력: ')
                if format == '회원 비밀번호':
                    self.member_format[format] = self.hashing(self.member_format[format])
            self.members.append(
                Member(*[self.member_format[format] for format in self.member_format.keys()])
            )
            if input('더 추가하시겠나요?(y/n): ') == 'n': break

        return True

    def post_list(self):
        for post in self.posts:
            post.display()

        return True

    def post_append(self):
        for format in self.post_format.keys():
            self.post_format[format] = input(f'{format}을 입력: ')
        self.posts.append(
            Post(*[self.post_format[format] for format in self.post_format.keys()])
        )

        return True

    def post_search(self):
        search = input('검색어 입력: ')
        for post in self.posts:
            if search in post.content:
                post.display()
        return True

    def quit(self):
        return False

def main():
    comm = Community()
    connect = True
    while connect:
        print('='*30)
        comm.print_opt()
        connect = comm.execute(input('> '))
        
    
main()