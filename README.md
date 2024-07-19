# Chat and Group Management API

This API provides endpoints for managing chat messages and groups within a Django application. It includes views for creating, retrieving, updating, and deleting chat messages and groups.

- **Chat Management:**
  - `ChatListCreateView`: Handles listing all chat messages and creating new messages.
  - `ChatDetailView`: Manages retrieval, updating, and deletion of individual chat messages. Includes custom handling for updating messages.
  - `ReplyToMessageView`: Allows partial updates to chat messages for replying to existing messages.

- **Group Management:**
  - `GroupListCreateView`: Lists all groups and allows creation of new groups.
  - `GroupDetailView`: Manages retrieval, updating, and deletion of individual groups.
