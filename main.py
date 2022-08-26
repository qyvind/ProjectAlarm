import pymssql
import time


if __name__ == '__main__':
    conn = pymssql.connect('fm-sql05', 'mf_byod_reader', 'lOBCeVgYOC1hDXsVrNzn', 'byod_staging')
    cursor = conn.cursor(as_dict=True)

    print('Sjekk prosjektnummer:')
    project = input()

    found = False
    while not found:
        cursor.execute(f"select * from  integration.vProdOrderWithOperation where prodid = \'{project}\'")
        result = cursor.fetchall()
        rows = len(result)
        print(f"Ser etter prosjekt {project}")
        if rows > 0:
            found = True
            print(f"************** Prosjekt {project} er kommet over i byod ****************")
        else:
            time.sleep(5)