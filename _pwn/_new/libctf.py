"""This file should not be modified"""
import pwn, re, time

class Pwnable(pwn.tube):
    debug = True
    test_challenges = {}
    query_regex = r""
    flag_regex = r""

    def detect_flag(self, line: str):
        match = re.match(self.flag_regex, line)
        if match:
            print("!" * 80)
            print(line)
            exit(0)

    def challenge(self):
        match = None
        timeout = 20
        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
            line = self.recvline(keepends=False).decode("utf-8").strip()
            self.detect_flag(line)

            if self.debug:
                print(line)
            
            match = re.match(self.query_regex, line)
            if match:
                break
            
            time.sleep(.05)
        return match

    def test(self, solve):
        fail=False
        for test in self.test_challenges:
            match = re.match(self.query_regex, test["challenge"].decode("utf-8"))
            res = str(solve(match)).encode("utf-8")
            if test["response"] != res:
                print(f"FAIL\t{test['challenge']}\t{test['response']}\t{res}")
                fail=True
            else:
                print(f"PASS\t{test['challenge']}\t{test['response']}\tPASS")
        if fail:
            exit(0)

    def response(self, response: bytes):
        if self.debug:
            print(response)
        self.sendline(response)


    def start(self, solve: callable):
        print("PWNING... PLEASE WAIT...")
        while True:
            match = self.challenge()
            self.response(str(solve(match)).encode("utf-8"))

class Remote(pwn.remote, Pwnable):
    pass    

class Local(pwn.process, Pwnable):
    pass