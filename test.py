from concurrent.futures import ThreadPoolExecutor
from concurrent.futures.thread import _worker
from xmlrpc.server import SimpleXMLRPCRequestHandler



def main():
    katet1 = float(input("Катет 1: "))
    katet2 = float(input("Катет 2: "))

    with ThreadPoolExecutor(max_workers=4) as executor:
        square_kat1 = executor.submit(pow, katet1, 2)
        square_kat2 = executor.submit(pow, katet2, 2)
        try:
            
            hypotenuse = executor.submit(pow, square_kat1.result()+square_kat2.result(), 0.5)
            print(hypotenuse.result())
        except Exception as err:
            print(err)
  


if __name__ == "__main__":
    main()
