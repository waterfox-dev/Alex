import 'package:alex_dart_library/src/client.dart';
import 'package:alex_dart_library/src/obj/author.dart';

void main() async {
  Client.baseUrl = "http://localhost:8000/";
  List<Author> authors = await Author.getAuthors();
  print(authors);

  Author author = await Author.getAuthor(1);
  print(author);
}
