#include <iostream>
#include <trivial/Entity.h>

int main()
{
	Trivial::Entity entity;

	entity.SetName("Hello, GYP");
	
	std::cout << entity.GetName() << std::endl;

	return 0;
}
