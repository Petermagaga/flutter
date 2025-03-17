import 'dart:convert';
import 'package:http/http.dart' as http;
import 'task_model.dart';

class ApiService {
  final String baseUrl = 'http:// 192.168.100.167/api/tasks/';

  /// Fetch all tasks
  Future<List<Task>> fetchTasks() async {
    final response = await http.get(Uri.parse(baseUrl));

    if (response.statusCode == 200) {
      List<dynamic> data = jsonDecode(response.body);
      return data.map((task) => Task.fromJson(task)).toList();
    } else {
      throw Exception('Failed to load tasks');
    }
  }

  /// Create a new task
  Future<Task> createTask(String title) async {
    final response = await http.post(
      Uri.parse(baseUrl),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"title": title, "completed": false}),
    );

    if (response.statusCode == 201) {
      return Task.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to create task');
    }
  }

  /// Update a task (mark complete/incomplete)
  Future<void> updateTaskStatus(int id, bool completed, String title) async {
  final String url = '$baseUrl$id/';  // Ensure trailing slash

  final response = await http.put(
    Uri.parse(url),
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonEncode({
      "title": title,   // Include title in the request
      "completed": completed,  
    }),
  );

  if (response.statusCode == 200) {
    print("✅ Task Updated Successfully");
  } else {
    print("❌ Error: ${response.statusCode}, Response: ${response.body}");
  }
}
}
