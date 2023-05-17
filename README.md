# Presentation Notes

## Slide 1

## Slide 2
WHOAMI
- 	Where do I work
- 	What do we do | Team of 16

What do I do at my work
- 	Security Operation Center Developer aka The Dev Goon
- 	Cloud Engineer for software and technologies

---

What is this talk about:
- 	Threats are not complex anymore
- 	We some how can deal with large threats but not small ones
- 	What do we do moving forward

## Slide 3
**Optus**
- API did not require authentication/authorization to access it
- Sensitive information was available on the API

**Medibank**
- Compromised credentials - which usually is a tell tale sign of we simply got phished

**Log4j**
- Minecraft accident effecting major vendors and too many websites.
- Silly features enabled by default, JNDI allowing external script execution on the Host.

**OpenAI**
- Simple Cross Site Script attack allowing attackers to send links to their victims and steal their session.s
- Which in turn allows them to view all of their searches and queries to OpenAI.

## Slide 4
**API Analogy**
Restaurant ordering food/drinks

**JWT Analogy**
Restaurant requires ID to prove you are on the guest list

## Slide 5
Start the demonstration

- 	Log in as Adam
- 	Log in as Ian
- 	Pull out Adams JWT
- 	Visit jwt.io, show how the JWT functions
- 	Show reconnaissance for locating a hidden endpoint this would include
	-	Brute forcing endpoints
	-	Checking for documentation
	-	Discovering active protocols like http, https, PUT, DELETE, POST, GET
- 	Discover the lengthy string endpoint that reveals the key to the token.
	- 	Try a get request
	- 	Try a post request
	- 	Try posting my token
-	Use the /users endpoint to gain info about users
-	Now that I know the secret move back to jwt.io and create a new JWT token for another user.
- 	Use the /payment endpoint to send money to myself.
-	Sign back into my account and show the results. 

## Slide 6
**Number of Scams**
As seen here Australia gets a lot more scams but there are many that is known by Malaysia that are not shared on public websites. At least none that I was able to find.

**Percent of businesses surveyed experienced cyber attacks**
Hong Kong---43%
Indonesia---52%
Japan-------52%
Singapore---46%

Half of all these reported incidents had actual data loss occur. 

**Solution priority**
Australia favours very minorly money, tooling and training.

Malaysia favours monitoring (Verry good), moving off prem, and increasing the budget.

Sadly both do not value seeking specialist help abroad or within country.


## Slide 7
**Bad design and development**
-	Specialists or conducive testing should be done before letting your product is public.

**Priorities**
- 	Spending money on endless solutions wont work if we are missing the 
	specialists to implement them.

- 	Training is only relevant when you know your workforce is actually lacking.

-	Response plans, 39% of companies in Oceania have response plans ready in the event of a cyber attack.

**Communication**
-	There is not enough information when breaches occur. Researchers have 
	nothing to prevent it happening to others. These vulnerabilities vanish into the ether without remedy.