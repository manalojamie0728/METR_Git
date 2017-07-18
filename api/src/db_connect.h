#ifndef DB_CONNECT_H_
#define DB_CONNECT_H_

//#include "OTTI/ott_integrator/src/mysql_conn_pool.h"

using namespace std;

class DB_Connect// : public MySQLConnPool
{
private:
	string pool;

public:
	virtual ~DB_Connect();
	void borrow();
	void get_product(string msisdn, string keyword);
	void post_product(string msisdn, string keyword);
	void updone_product(string msisdn, string keyword);
};

#endif