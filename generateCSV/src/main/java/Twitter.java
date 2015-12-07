import java.util.List;
import java.util.ArrayList;


public class Twitter {
	class Entity {
		HashTag[] hashtags;
		User[] user_mentions;
		URL[] urls;
		class HashTag {
			public String text;
			@Override
			public String toString() {
				return text;
			}
		}
		class User{
			public String screen_name;
			@Override
			public String toString() {
				return screen_name;
			}
		}
		class URL{
			public String expanded_url;
			@Override
			public String toString() {
				return expanded_url;
			}
		}
		public List<String> getHashTags() {
			List<String> result = new ArrayList<String>();
			for (HashTag tag: hashtags) {
				result.add(tag.toString());
			}
			return result;
		}
		public List<String> getUrls() {
			List<String> result = new ArrayList<String>();
			for (URL tag: urls) {
				result.add(tag.toString());
			}
			return result;
		}
		public List<String> getUsers() {
			List<String> result = new ArrayList<String>();
			for (User tag: user_mentions) {
				result.add(tag.toString());
			}
			return result;
		}
	}
	
	public String text;
	public String id;
	public String lang;
	public String created_at;
	public Entity entities;
}
