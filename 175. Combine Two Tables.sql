/*
* @Author: zengjq
* @Date:   2020-05-21 13:34:08
* @Last Modified by:   zengjq
* @Last Modified time: 2020-05-22 09:04:12
*/
select FirstName, LastName, City, State from Person left join Address on Person.PersonId = Address.PersonId