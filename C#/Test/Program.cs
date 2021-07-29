using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
namespace Test
{
class Person
{
public string Name;
public int Age;
}
class Program
{

static void Main(string[] args)
{
List<Person> persons = new List<Person> {
new Person { Name = "Taro", Age = 25},
new Person { Name = "Jiro", Age = 22},
new Person { Name = "Saburo", Age = 19},
new Person { Name = "Shiro", Age = 16},
};
var nage = persons.Where(person => person.Age >= 20).Select(pr => new { pr.Name } );
foreach (var item in nage)
{
    Console.WriteLine(item);
}
}

}

}