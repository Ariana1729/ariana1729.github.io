facts = [2,2,3,11,11,19,47,71,3449,11953,5485619,2035395403834744453,17258104558019725087,1357459302115148222329561139218955500171643099]
sk = 496376126967937389571976109422637980673504661082365672441208505312035527818355270399022992839175993066806
assert prod(facts) == 2*sk

k = '''
000bfdc32162934ad6a054b4b3db8578674e27a165113f8ed018cbe9112
4fbd63144ab6923d107eee2bc0712fcbdb50d96fdf04dd1ba1b69cb1efe
71af7ca08ddc7cc2d3dfb9080ae56861d952e8d5ec0ba0d3dfdf2d12764
'''.replace('\n', '')


for i in subsets(facts):
    y = prod(i)+1
    x = 2*sk/(y-1)-1
    x = hex(x)[2:]
    y = hex(y)[2:]
    if abs(len(x)-len(y))<2 and (len(x)+len(y))%2==0:
        flag = bytes.fromhex(x+y)
        if b"CCTF" in flag:
            print(flag)
