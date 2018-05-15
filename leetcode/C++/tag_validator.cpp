// using state space is a beautiful solution to this problem

enum State { None, End, InContent, InBeginTag, InEndTagRead, InEndTagSlashRead, InCDATA};

class TagValidator {
	
public:
	string* bufferedChars;
	stack<string*> bufferedTags;
	State state;

	TagValidator() : bufferedChars(nullptr), bufferedTags(), state(None) {
		
	}

	~TagValidator() {
		if (bufferedChars != nullptr)
			delete bufferedChars;

		while (!bufferedTags.empty()) {
			auto ptr = bufferedTags.top();
			delete ptr;
			bufferedTags.pop();
		}
	}

	bool pushChar(char ch) {
		
		switch (state)
		{
		case None:
			return pushCharOnNone(ch);
		case End:
			return ch == ' ';
		case InBeginTag:
			return pushCharOnStartTag(ch);
		case InContent:
			return pushCharOnContent(ch);
		case InEndTagRead:
			return pushCharOnEndTagRead(ch);
		case InEndTagSlashRead:
			return pushCharInEndTagSlashRead(ch);
		case InCDATA:
			return pushCharOnCDATA(ch);
		default:
			break;
		}
	}

	const string CDATA = "[CDATA[";
	bool pushCharOnCDATA(char ch) {
		int length = bufferedChars->size();
		if (length <=6 && ch != CDATA[length])
			return false;

		if (ch == '>') {
			if ((*bufferedChars)[length - 1] != ']' || (*bufferedChars)[length - 2] != ']') 
				// still in CDATA
				return true;
			delete bufferedChars;
			bufferedChars = nullptr;
			state = bufferedTags.empty() ? End : InContent;
			return true;
		}
		bufferedChars->push_back(ch);
		return true;
	}

	bool pushCharOnContent(char ch) {
		if (ch != '<')
			return true;
		state = InEndTagRead;
		bufferedChars = new string();
		return true;
	}

	bool pushCharOnEndTagRead(char ch) {
		if (ch == '/')
		{
			state = InEndTagSlashRead;
			return true;
		}
		else if (ch == '!') {
			state = InCDATA;
			return true;
		}
		else {
			state = InBeginTag;
			return pushChar(ch);
		}
	}

	bool pushCharInEndTagSlashRead(char ch) {
		if (ch == '>')
		{
			if (*bufferedChars == *bufferedTags.top()) {
				delete bufferedTags.top();
				delete bufferedChars;
				bufferedChars = nullptr;
				bufferedTags.pop();

				state = bufferedTags.empty() ? End : InContent;
				return true;
			}
			else {
				return false;
			}
		}

		bufferedChars->push_back(ch);
		
		return true;
	}

	bool pushCharOnStartTag(char ch) {
		if (isupper(ch)) {
			if (bufferedChars->size() >= 9)
				return false;
			bufferedChars->push_back(ch);
			return true;
		}

		if (ch == '>') {
			state = InContent;
			if (bufferedChars->size() == 0)
				return false;
			bufferedTags.push(bufferedChars);
			bufferedChars = nullptr;
			return true;
		}
		return false;
	}

	bool pushCharOnNone(char ch) {
		if (ch == ' ')
			return true;
		if (ch != '<') return false;

		state = InBeginTag;
		bufferedChars = new string();

		return true;
	}

	bool isEmpty() {
		return bufferedChars == nullptr && bufferedTags.empty();
	}
};

class Solution {
public:

	bool isValid(const string& code) {
		TagValidator validator;
		for (char ch : code) {
			if (!validator.pushChar(ch))
				return false;
		}

		return validator.isEmpty();
	}


};