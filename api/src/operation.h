#ifndef OPERATION_H_
#define OPERATION_H_

//#include "OTTI/ott_integrator/src/ott_operations.h"

using namespace std;

class Operation//: public OTTOperations
{
private:
	string host;
	string db_name;
	string user;
	string password;

public:
	virtual ~Operation();
	int provision(string msisdn, string keyword);
	int deprovision(string msisdn, string keyword);
	int deprovision(string msisdn);
	int status(string msisdn, string keyword);
	int list_subscribed(string msisdn);
};

#endif