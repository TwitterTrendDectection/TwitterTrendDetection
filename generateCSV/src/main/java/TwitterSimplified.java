import java.util.ArrayList;
import java.util.List;


public class TwitterSimplified {
	public String text;
	public String id;
	public String created_at;
	public List<List<String>> hash_tags;
	public List<List<String>> urls;
	public List<List<String>> user_mentions;
	public TwitterSimplified(Twitter t) {
		text = t.text;
		id = t.id;
		created_at = t.created_at;
		hash_tags = new ArrayList<List<String>>();
		urls = new ArrayList<List<String>>();
		user_mentions = new ArrayList<List<String>>();
		hash_tags.add(t.entities.getHashTags());
		urls.add(t.entities.getUrls());
		user_mentions.add(t.entities.getUsers());
	}
}
