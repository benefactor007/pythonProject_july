#! /usr/bin/python3.5
"""
expect需要转义的符号列表
\ 需转义为 \\\
} 需转义为 \}
[ 需转义为 \[
$ 需转义为 \\\$
` 需转义为 \`
" 需转义为 \\\"

"""
import pexpect
import sys
from auto_write_otp_v20220516 import greenFont, repr_message,redFont
import time


if __name__ == '__main__':
    # print(len(sys.argv))
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = input("please input the serial num or Fazit-id:")
    log_file = log_file + "_log_file_" +".txt"
    with open(log_file, 'a') as my_log_file:
        p_command = "sudo minicom"
        p_minicom = pexpect.spawn(command=p_command, timeout=None, logfile= my_log_file, encoding='utf-8')
        i = p_minicom.expect(["password for jpcc",pexpect.EOF , pexpect.TIMEOUT])
        if i == 0:
            try:
                p_minicom.timeout = 5
                p_minicom.sendline("jpcc")
                p_minicom.expect("Welcome to minicom")
                p_minicom.sendline("PWC:")
                p_minicom.expect("pwc rx mode")
                p_minicom.sendline("cS 1 88")
                # p_minicom.expect("C0 88 00 11 00 02 00 FF FF FF FF FF FF FF 00 FF")
                p_minicom.sendline("pwc_config\[1\]")
                # time.sleep(2)
                print(greenFont(repr_message("Close the R7 log successfully")))
            except pexpect.TIMEOUT:
                # write_status = False
                print(p_minicom.before, p_minicom.after)
                print(redFont(repr_message("Timeout in minicom")))
            except pexpect.EOF:
                print(redFont(repr_message("Error in minicom")))
        else:
            print("Error")
        p_minicom.close()