#include <iostream>
#include <trivial/Entity.h>

int main()
{
	// MSVC 2013 is not supported yet.
	//static_assert(__cplusplus == 201103L), "C++11 supported.");

	Trivial::Entity entity;

	entity.SetName("Hello, GYP");
	std::cout << entity.GetName() << std::endl;

	return 0;
}
