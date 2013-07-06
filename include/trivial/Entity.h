#include <string>

namespace Trivial {

class Entity
{
public:
	char const* GetName() const;
	void SetName(char const* name);
private:
	std::string name;
};

}// namespace Trivial
