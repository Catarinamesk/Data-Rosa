from faker import Faker
import pandas as pd

data = {}
fake = Faker()
Faker.seed(0) 
locs= []
line = 'default'
cols = ["name","email", "username","phone_number", "address", "URL", "last_updated", "birthdate", "company","locale", "currency","timezone", "credit_card_provider", "credit_card_number","product_code"]

for _ in range(250):
	locs.append(fake.unique.locale())

print("generating fake data ...")
	
for i in range(250):
		l= locs[i]
		try:
				# data transformation: create the field country from locale; age from birth_date; full name;
				data = {
										"name" : [(fake.unique.first_name() + " " + fake.unique.last_name()) for i in range(250)],
										"username": [fake.user_name() for i in range(250)],
										"email" :[fake.unique.email() for i in range(250)],
										"phone_number" : [fake.unique.phone_number() for i in range(250)],
										"address" : [fake.unique.address() for i in range(250)],
										"currency" : 	[fake.currency() for i in range(250)],
										"URL": [fake.unique.url() for i in range(250)], 
										"last_updated": [fake.unique.date_time_between(start_date='-5y', end_date='now') for i in range(250)], 
										"birthdate": [fake.unique.date_of_birth() for i in range(250)],
										"locale" :  [fake.unique.locale() for i in range(250)], 
										"company":  [fake.unique.company() for i in range(250)],
										"timezone":  [fake.unique.timezone() for i in range(250)],
										"credit_card_provider":[fake.credit_card_provider() for i in range(250)],
										"credit_card_number":[fake.unique.credit_card_number() for i in range(250)],
										"product_code": [fake.license_plate() for i in range(250)]

				}
		except:
					fake.unique.clear()

df = pd.DataFrame(data)
df.head(5)
df.to_excel("fake-data.xlsx", columns=cols, index=False)

assert len(set(data)) == len(data)
print("DONE: generated fake data.")