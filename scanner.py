import sys
import requests

def scan():
    url = sys.argv[1]
    filename = sys.argv[2]
    file_find = sys.argv[3]
    num_not_found = 0
    array_success = []
    with open(filename,'r') as fd:
        for line in fd:
            new_line = line.strip('\n')
            new_url = url + new_line + file_find
            r = requests.get(new_url)
            response = 'URL:{} , Code:{}\n'.format(new_url, r.status_code)
            if r.status_code == 200:
                array_success.append(response)
            else:
                num_not_found+=1
            print(response)
    print('=======================================')
    print('Number of Not Found: {}'.format(num_not_found))
    print('=======================================')
    print('Found: ')
    for res in array_success:
        print('Result: {}'.format(res))

def main():
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <url> <domain_list> <target>")
        sys.exit()
    scan()

if __name__ == "__main__":
    main()
