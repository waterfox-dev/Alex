import 'dart:convert';
import 'dart:io';

import 'package:alex_dart_library/src/client.dart';
import 'package:http/http.dart' as http;

class Author {
  final int id; 
  final String name;
  final String firstname;

  Author({
    required this.id, 
    required this.name,
    required this.firstname
  }); 

  factory Author.fromJson(Map<String, dynamic> json) {
    return Author(
      id: json['id'],
      name: json['name'],
      firstname: json['first_name']
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'firstname': firstname
    };
  }

  static Future<List<Author>> getAuthors() async {
    Uri url = Uri.parse('${Client.baseUrl}api/authors');
    http.Response response = await http.get(url);
    List<Author> authors = [];
    if (response.statusCode == HttpStatus.ok) {
      List<dynamic> data = jsonDecode(response.body);
      for (var element in data) {
        authors.add(Author.fromJson(element));
      }
    }
    return authors;
  }

  static Future<Author> getAuthor(int id) async{
    Uri url = Uri.parse('${Client.baseUrl}api/authors/$id');
    http.Response response = await http.get(url);
    Author author = Author(id: 0, name: '', firstname: '');
    if (response.statusCode == HttpStatus.ok) {
      Map<String, dynamic> data = jsonDecode(response.body);
      author = Author.fromJson(data);
    }
    return author;
  }

  @override
  String toString() {
    return 'Author{id: $id, name: $name, firstname: $firstname}';
  }
}