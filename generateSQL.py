#!bin/python3

class table():

    def __init__(self, script_path, table_name):
        '''
        - table_name: table name
        - script_path: sql file path
        '''
        self.script_path = script_path
        self.name = table_name
        with open(self.script_path, "a") as f:
            f.write(
                f"---------- creating table  {self.name} ------------------\n")

    def createTable(self, attributes):
        '''
        - attributes: dictionary of attributes with their types
        '''
        with open(self.script_path, "a") as script:
            if (attributes):

                list_of_attributes = list(attributes.items())

                # start table creation
                script.write(
                    f'CREATE IF NOT EXIST TABLE {self.name} {"{"} {str(list_of_attributes[0][0]).upper()} {str(list_of_attributes[0][1]).upper()},\n')

                for (k, v) in list_of_attributes[1:len(attributes.items())-1]:
                    # write attributes
                    script.write(
                        f'\t {str(k).upper()} {str(v).upper()},\n')

                # write the last attribute
                script.write(
                    f'{str(list_of_attributes[-1][0]).upper()} {str(list_of_attributes[-1][1]).upper()} {"}"}\n\n')

            # close file
            script.close()


if __name__ == '__main__':

    # define table name
    table_name = "table1"

    # define attributes
    attrs = {
        "attr1": "INT",  # you should specify the type of the attribute based on the types that are supported on MySQL Server
        "attr2": "VARCHAR",
    }

    table_obj1 = table('sql_script1.sql', table_name)

    table_obj1.createTable(attrs)

    define_list_of_tables = ["table1", "table2", "table3"]

    script = "script2.sql"
    for tb in define_list_of_tables:
        attributes = {
            "attr1": "INT",  # you should specify the type of the attribute based on the types that are supported on MySQL Server
            "attr2": "VARCHAR",
        }

        table_obj2 = table(script, tb)
        
        table_obj2.createTable(attributes)
