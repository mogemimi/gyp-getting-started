#include <trivial/Entity.h>

namespace Trivial {

char const* Entity::GetName() const
{
	return name.c_str();
}

void Entity::SetName(char const* name)
{
	this->name = name;
}

}// namespace Trivial
