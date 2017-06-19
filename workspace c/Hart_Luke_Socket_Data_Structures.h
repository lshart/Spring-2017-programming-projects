#define MAX_NAME_LENGTH 20
#define IP_ADDRESS_LENGTH 16
#define MAX_CONTACT_LIST_SIZE 20
#define MAX_NUM_OF_CONTACT_LISTS 20

typedef struct
{
  char contactListName[MAX_NAME_LENGTH];
  char contactNamesList[MAX_CONTACT_LIST_SIZE][MAX_NAME_LENGTH];
  char ipList[MAX_CONTACT_LIST_SIZE][IP_ADDRESS_LENGTH];
  unsigned short portNumberList[MAX_CONTACT_LIST_SIZE];
} ContactList;
