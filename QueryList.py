import BDConnectionPool as Cp


def country():
    col = Cp.connection_pool()
    query = col.find({"Country_name"})
    return query
