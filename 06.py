def findPeak(n, l=None, r=None):
    if l is None and r is None:
        l, r = 0, len(n) - 1
    mid = (l +r) // 2
    if ((mid == 0 or n[mid - 1] <= n[mid]) and
            (mid == len(n) - 1 or n[mid + 1] <= n[mid])):
        return mid
    if mid - 1 >= 0 and n[mid - 1] > n[mid]:
        return findPeak(n, l, mid - 1)
    return findPeak(n, mid + 1, r)
def findPeakElement(n) -> int:
    if not n:
        exit(-1)
 
    index = findPeak(n)
    return n[index]
 
 
if __name__ == '__main__':
 
    n = [ 1, 7, 8, 9, 10, 2, 5, 6]
    print('The peak element is', findPeakElement(n))