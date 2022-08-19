def subarr_cnt(size):
    return ((size*(size+1))>>1)

def bin_or_sum(A, bit_pos):
    bin_or_sum = subarr_cnt(len(A))
    zero_cnt = 0
    for num in A:
        bin_val = (num>>bit_pos)&1
        if bin_val:
            bin_or_sum -= subarr_cnt(zero_cnt)
            zero_cnt = 0
        else:
            zero_cnt += 1
    
    if zero_cnt:
        bin_or_sum -= subarr_cnt(zero_cnt)
    
    return bin_or_sum

def main(A):
    MOD = 10**9 + 7

    N = len(A)
    max_A = max(A)

    bit_pos = 0
    total_bin_or_sum = 0

    while(max_A>>bit_pos):
        bit_pos_or_sum = bin_or_sum(A, bit_pos)
        total_bin_or_sum += bit_pos_or_sum<<bit_pos
        print(bit_pos, bit_pos_or_sum)
        bit_pos += 1

    ans = total_bin_or_sum%MOD

    return ans

if __name__=='__main__':
    A = [2, 0, 0, 2, 0, 2]
    ans = main(A)

    print(ans)